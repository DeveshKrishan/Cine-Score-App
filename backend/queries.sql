-- Grab all info about a movie
SELECT * FROM Movies

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
		WHERE f.Username = 'User1'
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