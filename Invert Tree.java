public static void main(String[] args) {
// write your code here

    TreeNode node1 = new TreeNode(1);
    TreeNode node2 = new TreeNode(2);
    TreeNode node3 = new TreeNode(3);
    TreeNode node4 = new TreeNode(4);
    TreeNode node5 = new TreeNode(5);
    TreeNode node6 = new TreeNode(6);
    TreeNode node7 = new TreeNode(7);
    TreeNode node8 = new TreeNode(8);
    TreeNode node9 = new TreeNode(9);

    node4.left = node2;
    node4.right = node7;

    node2.left = node1;
    node2.right = node3;

    node7.left = node6;
    node7.right = node9;


    TreeNode tmp = invertTree(node4);

    System.out.println(tmp.left.left.val);

    // int result = nthUglyNumber(8);

    // System.out.println(mySqrt(4));
}


public static TreeNode invertTree(TreeNode root) {

    if(root == null) {
        return null;
    }

    // System.out.println(root.val);

    TreeNode leftNode = invertTree(root.left);
    TreeNode rightNode = invertTree(root.right);

    TreeNode temp = leftNode;

    root.left = rightNode;
    root.right = leftNode;

    return root;
}
