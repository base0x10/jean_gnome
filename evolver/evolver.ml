open Core

let workingdir = "./workspace/"

(*
 * Evolution:
 * For an out of date but wonderful explination of technical aspects of genetic algorithms:
 *      http://sepwww.stanford.edu/public/docs/sep112/gabriel1/paper_html/index.html
 *
 * Parameters:
 *      POPSIZE
 *      ELITESIZE
 *      BUILTINPARENT
 *
 * At the start of each round, each of the members of the population is given a fitness score.
 *
 * The ELITESIZE fittest in this population are the initial members of the new population.
 * These can still be parents, but will also go unmodified into the new population
 *
 * Next, two elements of the population are chosen at random.  The one with the highest fitness
 * score is able to becomme a parent.  There is some chance rather than using this way of
 * choosing a parent, a parent will be either random bits or a vector of zeros.  
 *
 * When two parents have been chosen, a number of crossover points is chosen.  The number of
 * crossover points is the number of leading zeros of a random integer plus one. 
 * The actual points of cross over are also chosen randomly.  
 *
 * The intervals between crossover points are taken to be from alternating parents.
 * In this way children are constructed.
 *
 * When a child is contructed, it is immediatly checked for if it is stillborn.  If it is,
 * it is discarded, and if it is not, it goes into the new population.
 *
 * When the elitists and children equal POPSIZE, the next round begins.  
 *
 * For the first round, the only parents are random and zeros.  
 *
 *)

(*
 *
 *
 *)

let write_warrior (buf: Buffer.t)  = 
  let f = Out_channel.create  "file.foo" in
  Core.write_buf buf f

let buf = Buffer.create 402
let () = 
  let buf =  Buffer.create 402 in 
  write_warrior buf
  (* print_endline "It's the end of the world as we know" *)
