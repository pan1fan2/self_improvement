import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np

class TransferModel(object):
    def __init__(self):
       # 定义训练和测试图片的变化方法，标准话以及数据增强
       self.train_generator = ImageDataGenerator(rescale = 1./255.0)
       self.test_generator = ImageDataGenerator(rescale = 1./255.0)
       # 指定训练数据和测试数据的目录
       self.train_dir = "data/re/train"
       self.test_dir = "data/re/test"
       # 定义图片训练相关网络参数
       self.image_size = (224,224)
       self.batch_size = 32
       #定义迁移学习的基类模型
       #不包含VGG当中3个全连接层的几模型加载并且加载了参数
       #vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5
       self.base_model = tf.keras.applications.vgg16.VGG16(weights='imagenet',include_top=False)

       self.label_dict = {
           '0' : 'bus',
           '1' : 'dinosaurs',
           '2' : 'elephants',
           '3' : 'flowers',
           '4' : 'horse'
       }

    def get_local_data(self):
        """
        读取本地的图片数据以及类别
        :return: 训练数据和测试数据迭代器
        """
        #使用flow_from_directory
        train_gen = self.train_generator.flow_from_directory(directory=self.train_dir,
                                                target_size=self.image_size,
                                                batch_size=self.batch_size,
                                                class_mode="binary",
                                                shuffle=True)
        test_gen = self.test_generator.flow_from_directory(directory=self.test_dir,
                                                target_size=self.image_size,
                                                batch_size=self.batch_size,
                                                class_mode="binary",
                                                shuffle=True)    
        return train_gen ,test_gen  

    def refine_base_model(self):
        """
        微调vgg结构，5blocks后面+全局平均池化（减少迁移学习的参数数量）+ 两个全连接层
        """
        #1、获取原notop模型得出
        #[?,?,?,512]
        x = self.base_model.outputs[0]

        # 2、输出后面增加我们的自己定义的结构
        # [?,?,?,512] -> [?,1 * 1 * 512]
        x = keras.layers.GlobalAveragePooling2D()(x)

        #定义新的迁移模型
        x = keras.layers.Dense(1024,activation = tf.nn.relu)(x)
        y_predict = keras.layers.Dense(5,activation = tf.nn.softmax)(x)

        #model定义新模型
        #VGG 模型的输入， 输出 ： y_predict
        transfer_model = keras.models.Model(inputs = self.base_model.inputs, outputs = y_predict)

        return transfer_model

    def freeze_model(self):
        """
        冻结VGG模型(5blocks)
        冻结VGG的多少，根据你的数据量
        """
        # self.base_model.layers 获取所有层，返回层的列表
        for layer in self.base_model.layers:
            layer.trainable = False
    
    def compile(self,model):
        """
        编译模型：
        """
        model.compile(optimizer = tf.keras.optimizers.Adam(),
                    loss = tf.keras.losses.sparse_categorical_crossentropy,
                    metrics = ['accuracy'])
        return None
    
    def fit_generator(self,model,train_gen,test_gen):
        """
        训练模型，model.fit_generator() 不是选择model.fit()
        """
        modelckpt = keras.callbacks.ModelCheckpoint('ckpt/transfer_{epoch:02d}-{val_loss:.2f}.h5',
                                        monitor = 'val_accuracy',
                                        save_weights_only = True,
                                        save_best_only = True,
                                        mode = 'auto',
                                        period = 1)

        model.fit_generator(train_gen,epochs = 3,validation_data = test_gen, callbacks = [modelckpt])
    
    def predict(self,model):
        """
        预测类型
        """
        #加载模型， transfer_model
        model.load_weights("./ckpt/transfer_03-0.20.h5")
        #读取图片，处理
        image = load_img("./data/re/test/dinosaur/400.jpg",target_size=(224,224))
        image = img_to_array(image)
        #print(image.shape)
        #四维（224，224，3）-> （1，224，224，3）
        image = image.reshape([1,image.shape[0],image.shape[1],image.shape[2]])
        #print(image)

        #预测结果进行处理
        image = preprocess_input(image)
        predictions = model.predict(image)
        #print(predctions)

        res = np.argmax(predictions,axis = 1)
        print(self.label_dict[str(res[0])])



if __name__ == "__main__":
    tm = TransferModel()
    train_gen, test_gen = tm.get_local_data()
    model = tm.refine_base_model()
    # 训练
    # tm.freeze_model()
    # tm.compile(model)
    # tm.fit_generator(model,train_gen,test_gen)
    # 测试
    model = tm.refine_base_model()
    tm.predict(model)