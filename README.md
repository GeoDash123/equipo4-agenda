classDiagram
    class User {
        +id: int
        +name: str
        +email: str
    }

    class Book {
        +id: int
        +title: str
        +author: str
    }

    class Loan {
        +id: int
        +user_id: int
        +book_id: int
        +date: str
    }

    User --> Loan
    Book --> Loan