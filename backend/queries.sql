--write a query to get list of friend names for a user and the date they became friends given a username--
SELECT User2Username
		,FriendshipStarted
FROM Friends 
WHERE User1Username = 'User1'

--write a query to get user's favorite movies given a username--
SELECT m.MovieName
FROM Movies m
	INNER JOIN
		Favorites f
		ON m.MovieId = f.MovieId
		WHERE f.Username = 'User'
GROUP BY
	m.MovieName
--write a query to get all the reviews a user did along with its information given a username--
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
WHERE u.Username = 'User1'
GROUP BY m.MovieName
			,m.MovieYear
			,r.Score
			,r.ReviewDate
-- write a query to get the average rating for a movie given a movie id --
SELECT m.MovieName
		,AVG(r.Score)
FROM Reviews r
	INNER JOIN
		Movies m
		ON m.MovieId = r.MovieId
		WHERE m.MovieID = 'MovieID'
GROUP BY r.Score
--write a query to get the average rating a user gives in their reviews given a username--
SELECT u.Username
		,AVG(r.Score)
FROM Reviews r
INNER JOIN
	[User] u
	ON r.Username = u.Username
	WHERE u.Username = 'Username'
	GROUP BY u.Username
--write a query to get a movies information given a movieid--
SELECT m.MovieName
		,m.MovieYear
		,mg.Genre
FROM Movies m
INNER JOIN
	MovieGenre mg
	ON m.MovieId = mg.MovieGenreId
	WHERE m.MovieId = 'MovieID'
	GROUP BY m.MovieName
--write a query to check if given a username, is the username already in the user table given a username--
SELECT U.Username
FROM [User] u
WHERE U.Username = 'Username'