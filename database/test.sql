CREATE TABLE User (
    UserName NOT NULL PRIMARY KEY VARCHAR(255),
    Passcode NOT NULL VARCHAR(255),
    Email NOT NULL UNIQUE VARCHAR(255),
    Active BIT -- Active represents if a user is online. Made for future updates
    Phone INT(11) --Future scaliblity. Can allow to create 2FA authentication.
);

CREATE TABLE UserFriends (

)