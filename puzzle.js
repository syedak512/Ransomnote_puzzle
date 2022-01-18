function puzzle(number) {
    // a loop to go thorough all the numbers from 1 to number in parameter
    for(i=1; i <= number; i++) {
        //this checks if the number is divided by 3 the reminder is 0
        //also checks if the number is divided by 5 the reminder is 0
        if(i % 3 == 0 && i % 5 == 0) {
            console.log('Fizz Buzz')
        }
        //this checks the numbers that does not fit in previous catagory
        //and checks if the number is divided by 5 the reminder is 0
        else if(i % 5 == 0) {
            console.log('Buzz ')
        }
        //this checks the numbers  that doesnot fit previous two catagory
        // and checks if the number is divided by 3 the reminder is 0
        else if(i % 3 == 0) {
            console.log('Fizz ')
        }
        //prints all other number which are not divisible by 5 or 3
        else {
            console.log(i)
        }
    }
 }
 puzzle(100)
 