extern crate csv;

use std::error::Error;
use std::fs::File;

fn main() {
    if let Err(e) = read_csv_file() {
        println!("Error: {}", e);
    }
}

fn read_csv_file() -> Result<(), Box<dyn Error>> {
    let file = File::open("2011picid.csv")?;
    let mut reader = csv::Reader::from_reader(file);

    for result in reader.records() {
        let record = result?;
        let name = &record[0];
        let age: u32 = record[1].parse()?;
        let city = &record[2];
        println!("Name: {}, Age: {}, City: {}", name, age, city);
    }

    Ok(())
}

