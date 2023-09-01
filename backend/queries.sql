--write a query to get list of friend names for a user and the date they became friends given a username--
-- WORKS --
SELECT User2Username
		,FriendshipStarted
FROM Friends 
WHERE User1Username = 'testUser'

--write a query to get user's favorite movies given a username--
-- WORKS --
SELECT f.Username
		,m.MovieName
FROM Movies m
	INNER JOIN
		Favorites f
		ON m.MovieId = f.MovieId
		WHERE f.Username = 'testUser'
GROUP BY
	m.MovieName
	,f.Username
--write a query to get all the reviews a user did along with its information given a username--
-- WORKS --
SELECT r.Username
			,m.MovieName
			,m.MovieYear
			,r.Score
			,r.ReviewDate
FROM Reviews r
	INNER JOIN
		Movies m
		ON r.MovieId = m.MovieId
	INNER JOIN
		[User] u
		ON r.Username = u.Username
WHERE u.Username = 'testUser'
GROUP BY m.MovieName
			,m.MovieYear
			,r.Score
			,r.ReviewDate
			,r.Username
-- write a query to get the average rating for a movie given a movie id --
-- WORKS --
SELECT m.MovieName
		,AVG(r.Score) AS 'Average Score'
FROM Reviews r
	INNER JOIN
		Movies m
		ON m.MovieId = r.MovieId
		WHERE m.MovieID = 1
		GROUP BY m.MovieName
--write a query to get the average rating a user gives in their reviews given a username--
-- WORKS --
SELECT u.Username
		,AVG(r.Score) AS 'Average Score'
FROM Reviews r
INNER JOIN
	[User] u
	ON r.Username = u.Username
	WHERE u.Username = 'testUser'
	GROUP BY u.Username
--write a query to get a movies information given a movieid--
-- WORKS --
SELECT m.MovieId
		,m.MovieName
		,m.MovieYear
		,mg.Genre
FROM Movies m
INNER JOIN
	MovieGenre mg
	ON m.MovieId = mg.MovieGenreId
	WHERE m.MovieId = 1
	GROUP BY m.MovieId
			,m.MovieName
			,m.MovieYear
			,mg.Genre
--write a query to check if given a username, is the username already in the user table given a username--
-- WORKS --
SELECT u.Username
FROM [User] u
WHERE u.Username = 'testUser'