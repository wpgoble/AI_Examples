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
                    double d_i1j = dist(x[curState[i1]], y[curState[i1]], 
                                        x[curState[j]], y[curState[j]]);
                    double d_ij1 = dist(x[curState[i]], y[curState[i]], 
                                        x[curState[j1]], y[curState[j1]]);
                    double d_i1i = dist(x[curState[i1]], y[curState[i1]], 
                                        x[curState[i]], y[curState[i]]);
                    double d_jj1 = dist(x[curState[j]], y[curState[j]], 
                                        x[curState[j1]], y[curState[j1]]);
                    double delta =  d_i1j + d_ij1 - d_i1i - d_jj1;

                    if (delta < bestDelta) {
                        bestDelta = delta;
                        best_I = i;
                        best_J = j;
                    }
                }
            }

            if (bestDelta < -1e-9) {
                reverse(curState, best_I, best_J);
                System.arraycopy(curState, 0, bestState, 0, n);
                repaint();

                try {
                    Thread.sleep(waitTime);
                } catch (InterruptedException e) {
                    // do nothing
                }
            } else {
                done = true;
            }
        }
    }

    // Reverse the order from i to j
    static void reverse(int[] p, int i, int j) {
        int n = p.length;
        while (i != j) {
            int t = p[j];
            p[j] = p[i];
            p[i] = t;
            i = (i + 1) % n;
            if (i == j) {
                break;
            }
            j = (j - 1 + n) % n;
        }        
    }

    double eval(int[] state) {
        double res = 0;
        for(int i = 0, j = state.length - 1; i < state.length; j = i++) {
            res += dist(x[state[i]], y[state[i]], x[state[j]], y[state[j]]);
        }
        return res;
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