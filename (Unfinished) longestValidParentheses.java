public static int longestValidParentheses(String s) {

    Stack<Character> stack = new Stack<Character>();

    int maxLength = 0;

    int currentLength = 0;

    for(int i = 0; i<s.length(); i++) {

        Character c = s.charAt(i);
        // System.out.println(c);

        if (c.equals('(')) {
            // System.out.println("push works");
            stack.push(c);
        } else {
            if (stack.isEmpty()) {

            } else {
                Character temp = stack.pop();
                if (temp.equals('(')) {
                    currentLength = currentLength + 2;
                }
            }

        }
        System.out.println(currentLength);
    }

    System.out.println(stack);
    return 0;
}
