use rand::Rng;
use std::collections::HashMap;

fn get_card_value() -> i32 {
  let mut rng = rand::thread_rng();
  return rng.gen_range(2..14);
}

fn get_card_str(card_value: i32) -> String {
  let arr = [(10, String::from("T")),(11, String::from("J")),(12, String::from("Q")),(13, String::from("K")),(14, String::from("A"))];
  let lookup: HashMap<_,_> = arr.iter().cloned().collect();
  match lookup.get(&card_value) {
    Some(s) => s.to_string(),
    _ => card_value.to_string()
  }
}

fn get_hl_guess() -> String {
  let mut guess = String::new();
  println!("Is the next card higher (h) or lower (l)?");
  loop {
    std::io::stdin().read_line(&mut guess).expect("uh oh!!!");
    guess = guess.trim().to_lowercase();
    if guess == "h" {
      return String::from("HIGH");
    } else if guess == "l" {
      return String::from("LOW")
    }
    println!("Please input either 'h' or 'l'");
    guess = String::new();
  }
}

fn get_bet_amount(maximum: i32) -> i32 {
  println!("Enter your bet (current total: {}) ", maximum);
  let mut raw = String::new();
  loop {
    std::io::stdin().read_line(&mut raw).expect("uh oh!!!");
    let bet: i32 = raw.trim().parse().expect("uh oh!!!");
    if bet > 0 && bet <= maximum {
      return bet;
    }
    raw = String::new();
    println!("Please enter a valid bet > 0 and <= your current total.");
  }
}

fn player_guess_correct(card1: i32, card2: i32, bet_type: String) -> bool {
  return (bet_type == "HIGH" && card2 > card1) || (bet_type == "LOW" && card2 < card1);
}

fn main() {
  let mut rounds = 0;
  let mut total = 100;
  while rounds < 10 && total > 0 {
    let card1 = get_card_value();
    let card2 = get_card_value();
    println!("The first card is: {}", get_card_str(card1));
    let player_guess = get_hl_guess();
    let player_bet = get_bet_amount(total);
    let round_result = player_guess_correct(card1, card2, player_guess);
    println!("The second card is: {}", get_card_str(card2));
    if round_result {
      total += player_bet;
      println!("Round won, gained {} points.", player_bet);
    } else {
      total -= player_bet;
      println!("Round lost, lost {} points.", player_bet);
    }
    println!("{}", total);
    rounds += 1;
  }
}
