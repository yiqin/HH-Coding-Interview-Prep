
public static void main(String[] args) {
// write your code her

    String[] strs = new String[]{"eat", "tea", "tan", "ate", "nat", "bat"};

    groupAnagrams(strs);

}

public static List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> results = new ArrayList<List<String>>();

    // Arrays.sort(strs);

    HashMap<Set<Character>, List<String>> hash = new HashMap<Set<Character>, List<String>>();

    for(int i=0 ; i< strs.length; i++) {

        Set<Character> key = stringToSet(strs[i]);
        List<String> value = hash.get(key);

        if (value == null) {
            List<String> newValue = new ArrayList<String>();
            newValue.add(strs[i]);
            hash.put(key, newValue);
        } else {
            value.add(strs[i]);
            // hash.put(key, value);
        }
    }

    System.out.println(hash.values());

    for(List<String> result : hash.values()) {
        results.add(result);
    }

    return results;
}

public static Set<Character> stringToSet(String str) {

    Set<Character> set = new HashSet<Character>();
    for(int i=0; i<str.length(); i++) {
        set.add(str.charAt(i));
    }

    return set;
}
