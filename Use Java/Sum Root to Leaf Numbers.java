    public static void main(String[] args) {
	// write your code here

        TreeNode node1 = new TreeNode(1);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(3);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(5);
        TreeNode node6 = new TreeNode(6);
        TreeNode node7 = new TreeNode(7);

        node1.left = node2;
        // node1.right = node3;
        node2.left = node4;
        node2.right = node5;
        // node3.left = node6;
        // node3.right = node7;

        sumNumbers(node1);
    }

    public static int sumNumbers(TreeNode root) {

        int sum = 0;

        sum = dfs(root, sum);

        System.out.println(sum);

        return sum;
    }

    public static int dfs(TreeNode node, int sum) {

        System.out.println(node.val);

        sum = sum*10+node.val;

        if (node.left == null && node.right == null) {
            return sum;

        }

        int subSum = 0;
        if (node.left != null) {
            subSum = dfs(node.left, sum);

        }

        if (node.right != null) {
            subSum = dfs(node.right, sum);

        }

        System.out.println("##############");
        System.out.println(sum+subSum);

        return sum + subSum;

    }