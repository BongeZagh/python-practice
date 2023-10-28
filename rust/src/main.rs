extern crate csv;

use std::error::Error;
use std::fs::File;
use std::path::Path;

fn main() {
    if let Err(e) = read_csv_file() {
        println!("Error: {}", e);
    }
}

fn read_csv_file() -> Result<(), Box<dyn Error>> {
    let current_dir = std::env::current_dir()?;
    let file_path = current_dir.join("2011picid.csv");
    let file = File::open(&file_path)?;
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

