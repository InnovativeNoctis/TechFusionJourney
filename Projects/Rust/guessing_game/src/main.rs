use rand::prelude::*;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("### Guessing Game ###");

    let secret_number = rand::rng().random_range(1..=100);

    loop { // Looping the users guess untill the win.
        println!("Secret number: {secret_number}");
        println!("Enter your guess: ");

        let mut guess: String = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too Small!"),
            Ordering::Greater => println!("Too Big"),
            Ordering::Equal => {
                println!("You Win!");
                break;
            }
        }
    }
}
