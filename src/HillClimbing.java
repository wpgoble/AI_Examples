// Code is originally from 
// https://sites.google.com/site/indy256/algo/simulated_annealing
// FOR DEMO USE ONLY

import javax.swing.*;
import java.util.Random;

public class HillClimbing extends JFrame implements Runnable {
    Random rand = new Random();
    int n = rand.nextInt(300) + 250;
    final int waitTime = 0;                     // milliseconds b/t repaining

    int[] bestState;
    double[] x = new double[n];
    double[] y = new double[n];

    public void setXYValues() {
        for(int i = 0; i < n; i++) {
            x[i] = rand.nextDouble();
            y[i] = rand.nextDouble();
        }
    }

    public void climb() {
        System.out.println("Hello, World");
    }

    @Override
    public void run() {
        setXYValues();
        climb();
    }
}