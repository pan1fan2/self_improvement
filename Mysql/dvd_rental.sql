-- Identiy top 10 customers and their email 
SELECT concat(first_name," ",last_name) as full_name, email,sum(p.amount) as total_amount_paid
FROM customer c
JOIN payment p on p.customer_id = c.customer_id
GROUP BY full_name, email
ORDER BY total_amount_paid DESC
Limit 10;

-- What are the most profitable movie genres?
SELECT c.name as genre, sum(p.amount) as total_sales
FROM category c
JOIN film_category fc on fc.category_id = c.category_id
JOIN film f on fc.film_id = f.film_id
JOIN inventory i on f.film_id = i.film_id
JOIN rental r on i.inventory_id = r.inventory_id
JOIN customer cus on r.customer_id = cus.customer_id
join payment p on r.rental_id = p.rental_id
GROUP BY genre
ORDER BY total_sales DESC;

-- Total sale by manager
SELECT concat(staff.first_name, " ", staff.last_name) as manager, sum(p.amount) as total_sales
FROM category c
JOIN film_category fc on fc.category_id = c.category_id
JOIN film f on fc.film_id = f.film_id
JOIN inventory i on f.film_id = i.film_id
JOIN rental r on i.inventory_id = r.inventory_id
JOIN customer cus on r.customer_id = cus.customer_id
join payment p on r.rental_id = p.rental_id
JOIN staff on p.staff_id = staff.staff_id
GROUP BY manager
ORDER BY total_sales DESC;

-- how many movies are returned late , early and on time?
select case
	when rental_duration > DATEDIFF(return_date , rental_date) then 'returned_early'
    when rental_duration = DATEDIFF(return_date , rental_date) then 'returned_on_time'
    else 'returned_late' end as return_status, count(*) as total_number
from film
join inventory on film.film_id = inventory.film_id
join rental on inventory.inventory_id = rental.inventory_id
group by return_status;

-- customr based countries
select country, count(customer_id) as totoal_number_customers
from country
join city on country.country_id = city.country_id
join address on city.city_id = address.city_id
join customer on address.address_id = customer.address_id
group by country
order by totoal_number_customers desc;

-- average rental rate per movie genre
select name as movie_genre,avg(rental_rate) as ave_rental_rate
from category 
join film_category using (category_id)
join film using (film_id)
group by movie_genre
order by ave_rental_rate desc;