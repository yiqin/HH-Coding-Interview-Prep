package com.company;

import java.lang.reflect.Array;
import java.sql.SQLSyntaxErrorException;
import java.util.ArrayList;
import java.util.*;
import java.util.Queue;
import java.util.regex.Matcher;

/**
 * Created by yiqin on 9/10/15.
 */
public class MergeIntervals {

    public static void main(String[] args) {

        List<Interval> intervals = new ArrayList<Interval>();

        Interval interval1 = new Interval(1, 3);
        Interval interval2 = new Interval(2, 6);
        Interval interval3 = new Interval(8, 10);
        Interval interval4 = new Interval(15, 18);

        intervals.add(interval1);
        intervals.add(interval2);
        intervals.add(interval3);
        intervals.add(interval4);


        merge(intervals);

    }

    public static List<Interval> merge(List<Interval> intervals) {








        return intervals;
    }

}
