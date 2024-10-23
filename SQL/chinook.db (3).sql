--1.3
/*SELECT *
FROM customers
WHERE Country = 'Brazil';
--1.4
SELECT * from employees
WHERE title = 'Sales Support Agent';
--1.5
select * from tracks
inner join  albums on albums.AlbumId = tracks.AlbumId
INNER join artists on albums.ArtistId = artists.ArtistId
where artists.Name = 'AC/DC';
--1.6
SELECT customerid, firstname || ' ' || lastname as Nombre_Completo, country AS País FROM customers
where country <> 'USA';
--1.7
SELECT firstname || ' ' || lastname AS NombreCompleto, city || ' ' || state || ' ' || country as Dirección, email from employees
WHERE title = 'Sales Support Agent';
--1.8
SELECT DISTINCT billingcountry FROM invoices;
select state, COUNT (customerid) from customers where customers = 'USA' GROUP by  'state' order by 2 DESC;
SELECT COUNT (quantity) FROM invoice_items
where invoiceid = '37';
--1.9
select DISTINCT COUNT name
from tracks
inner join albums on albums.AlbumId = tracks.AlbumId
INNER join artists on albums.ArtistId = artists.ArtistId
where artists.Name = 'AC/DC';
--1.10
SELECT COUNT (quantity) FROM invoice_items
GROUP by invoiceid;
--1.11
SELECT billingcountry, COUNT (invoiceid) from invoices
group by billingcountry
order by 2  Desc;
--1.12
select count (invoiceid)
from invoices
where invoicedate LIKE '2009%' or '2011%';
--1.13
select count (invoiceid)
from invoices
where invoicedate BETWEEN '2009%' and '2011%';
--1.14
select COUNT (customerid)
from customers
where country in ('Spain', 'Brazil');
--1.15
select name from tracks
where name like 'You%'
--2.1
select customerid, invoiceid, invoicedate, billingcountry
from invoices
inner JOIN invoices on invoices.CustomerId = customers.CustomerId
where invoices.billingcountry like 'Brazil'
--2.2
SELECT employees.FirstName || ' ' || employees.LastName AS SalesAgent, invoices.InvoiceId, invoices.InvoiceDate, invoices.Total
FROM invoices
INNER JOIN customers ON invoices.CustomerId = customers.CustomerId
INNER JOIN employees ON customers.SupportRepId = employees.EmployeeId
WHERE employees.Title = 'Sales Support Agent';
--2.3
SELECT customers.FirstName || ' ' || customers.LastName AS CustomerName, customers.Country, employees.FirstName || ' ' || employees.LastName AS SalesAgent, invoices.Total
FROM invoices
INNER JOIN customers ON invoices.CustomerId = customers.CustomerId
INNER JOIN employees ON customers.SupportRepId = employees.EmployeeId
WHERE employees.Title = 'Sales Support Agent';

--2.4
select tracks.name, invoice_itemsinvoiceid 
from invoice_items
INNER join tracks on invoice_items.TrackId = tracks.TrackId
INNER join invoices on invoice_items.InvoiceId = invoices.InvoiceId
--2.5
select tracks.name as Canción, albums.title As Álbum, genres.name AS Género, media_types.name AS Formato 
from tracks
inner join albums on tracks.AlbumId = albums.AlbumId
inner JOIN genres on tracks.GenreId = genres.GenreId
inner join media_types on tracks.MediaTypeId = media_types.MediaTypeId
--2.6
SELECT count (tracks.TrackId)
from playlist_track
INNER JOIN playlists on playlist_track.PlaylistId = playlists.PlaylistId
inner join tracks on playlist_track.TrackId = tracks.TrackId
--2.7
select employees.EmployeeId, invoices.Total
from customers
inner join employees on customers.SupportRepId = employees.EmployeeId
inner JOIN invoices  on customers.CustomerId = invoices.CustomerId
--2.8
select employees.EmployeeId, MAX(TOTAL)
from customers
inner join employees on customers.SupportRepId = employees.EmployeeId
inner JOIN invoices  on customers.CustomerId = invoices.CustomerId
where invoicedate = '2009%'
*/
--2.9
select SUM(invoices.Total, tracks.Composer)
from invoice_items
INNER join tracks on invoice_items.TrackId = tracks.TrackId
inner join invoices on invoices.InvoiceId = invoice_items.InvoiceId
order by Composer DESC