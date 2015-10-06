public static boolean isAnagram(String s, String t) {

    HashMap<Character, Integer> hm = new HashMap<Character, Integer>();

    for(int i = 0; i< s.length(); i++) {
        Character c = s.charAt(i);
        Integer tempC = hm.get(c);
        if (tempC == null) {
            hm.put(c, 1);
        } else {
            tempC++;
            hm.put(c, tempC);
        }
        // System.out.println(c);
        // System.out.println(hm.get(c));
    }

    for(int i = 0; i<t.length(); i++) {
        Character c = t.charAt(i);
        Integer temp = hm.get(c);
        if (temp == null) {
            return false;
        } else {
            temp--;
            if (temp == 0) {
                hm.remove(c);
            } else {
                hm.put(c, temp);
            }
        }
    }

    System.out.println(hm.size());

    if (hm.size() == 0) {
        return true;
    } else {
        return false;
    }

    // return true;
}
