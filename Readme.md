WELCOME TO TERMINAL JOURNAL MANAGEMENT SYSTEM (built in python without any database)





Instructions:
    1.to start application:
        1. uncomment line 178 i,e. createDatabse() while keeping rest of lines(179-181) commented 
        2.then run once to establish databse
        note:-can ignore above lines if databse already exists i,e(data_pick.pkl)
        3.now reverse the process i,e put line 178 commented while other three uncomment back.
        4.then you can run the application.
    1. simply follow the terminal instructions
    2.to test application:
        1.You can register 2-3 users
        2.Login one by one :check for authenticity
        3.create journals and view when logged in as different users
        4.You can have a look at your database table how it is being made.
    3.Note:
        1.Each time login or register or createJournal etc calls program consoles the object array that reside in our database
        2.to serialize data we use pickle module
        3.we use simple print formatter pprint module 