// Code is originally from 
// https://sites.google.com/site/indy256/algo/simulated_annealing
// FOR DEMO USE ONLY

import javax.swing.*;
import java.util.Random;

public class HillClimbing extends JFrame implements Runnable {
    Random rand = new Random();
    int n = rand.nextInt(300) + 250;
    final int waitTime = 0;                     // milliseconds b/t repaining

    public void climb() {
        System.out.println("Hello, World");
    }

    @Override
    public void run() {
        climb();
    }
}