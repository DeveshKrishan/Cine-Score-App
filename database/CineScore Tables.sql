CREATE TABLE [User]
(
	Username VARCHAR(20) NOT NULL
	,[Password] VARCHAR(30) NOT NULL
	,Email VARCHAR(60) NOT NULL
	,Active BIT NULL
	,Phone VARCHAR(15) NULL
	,PRIMARY KEY (Username)
)

CREATE TABLE Movies
(
	MovieId INT
	,MovieName VARCHAR(200)
	,MovieYear INT
	,PRIMARY KEY (MovieId)
)

CREATE TABLE Movie_Genre
(
	MovieId INT NOT NULL
	,Genre VARCHAR(20) NULL
	,PRIMARY KEY (MovieId)
	,FOREIGN KEY (MovieId) REFERENCES Movies(MovieId)
)

CREATE TABLE Reviews
(
	[Username] VARCHAR(20) NOT NULL
	,ReviewDate DATE NOT NULL
	,MovieId INT NOT NULL
	,Score FLOAT NOT NULL
	,PRIMARY KEY (MovieId,[Username])
	,FOREIGN KEY (MovieID) REFERENCES Movies(MovieId)
	,FOREIGN KEY ([Username]) REFERENCES [User](Username)
)

CREATE TABLE Favorites
( 
	[Username] VARCHAR(20) NOT NULL
	,MovieId INT NOT NULL
	,PRIMARY KEY(MovieId, [Username])
	,FOREIGN KEY (MovieID) REFERENCES Movies(MovieId)
	,FOREIGN KEY ([Username]) REFERENCES [User](Username)
)

CREATE TABLE Friends
(
	FriendshipId INT IDENTITY(1,1)
	,User1Username VARCHAR(20) NOT NULL
	,User2Username VARCHAR(20) NOT NULL
	,FriendshipStarted DATE NOT NULL
	,PRIMARY KEY(FriendshipId)
	,FOREIGN KEY (User1Username) REFERENCES [User](Username)
	,FOREIGN KEY (User2Username) REFERENCES [User](Username)
)
GO
