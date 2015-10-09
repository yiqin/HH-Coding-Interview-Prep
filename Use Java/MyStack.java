package com.company;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by yiqin on 8/28/15.
 */
public class MyStack {

    Queue<Integer> queue1 = new LinkedList<Integer>();
    Queue<Integer> queue2 = new LinkedList<Integer>();

    // Push element x onto stack.
    public void push(int x) {

        if(queue1.isEmpty() && queue2.isEmpty()) {
            queue1.add(x);
            return;
        }

        if(queue2.isEmpty()) {
            queue2.add(x);
            while(!queue1.isEmpty()) {
                int temp = queue1.poll();
                queue2.add(temp);
            }
        } else {
            queue1.add(x);
            while(!queue2.isEmpty()) {
                int temp = queue2.poll();
                queue1.add(temp);
            }
        }
        System.out.println("push.......");
        System.out.println(queue1.size());
        System.out.println(queue2.size());
    }

    // Removes the element on top of the stack.
    public void pop() {

        if(queue1.isEmpty() && queue2.isEmpty()) {
            return;
        }

        if(queue2.isEmpty()) {
            queue1.poll();
        } else {
            queue2.poll();
        }
    }

    // Get the top element.
    public int top() {
        if(queue1.isEmpty() && queue2.isEmpty()) {
            return 0;
        }

        if(queue2.isEmpty()) {
            return queue1.peek();
        } else {
            return queue2.peek();
        }

    }

    // Return whether the stack is empty.
    public boolean empty() {

        if (queue1.isEmpty() && queue2.isEmpty()){
            return true;
        } else {
            return false;
        }

    }

}
