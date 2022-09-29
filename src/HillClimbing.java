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

    public static void main(String[] args) {
        new HillClimbing();
    }

    public void setXYValues() {
        for(int i = 0; i < n; i++) {
            x[i] = rand.nextDouble();
            y[i] = rand.nextDouble();
        }
    }

    public void climb() {
        int[] curState = new int[n];

        for(int i = 0; i < n; i++) {
            curState[i] = i;
        }

        bestState = curState.clone();
        boolean done = false;

        while(!done) {
            double bestDelta = 0.0;
            int best_I = -1;
            int best_J = -1;

            for(int i = 0; i < n; i++) {
                for(int j = i+1; j < n; j++) {
                    int i1 = (i - 1 + n) % n;
                    int j1 = (j + 1) % n;
                    double delta = dist(x[curState[i1]], y[curState[i1]], 
                                        x[curState[j]], y[curState[j]]) 
                                    + dist()
                }
            }
        }
    }

    static double dist(double x1, double y1, double x2, double y2) {
        double dx = x1 - x2;
        double dy = y1 - y2;
        return Math.sqrt(dx * dx + dy * dy);
    }

    public HillClimbing() {
        new Thread(this).start();   // necessary for calling the run method.
    }

    @Override
    public void run() {
        setXYValues();
        climb();
    }
}