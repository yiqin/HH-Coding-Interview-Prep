public static void main(String[] args) {
// write your code her

    TreeNode root = new TreeNode(3);
    TreeNode val9 = new TreeNode(9);
    TreeNode val20 = new TreeNode(20);
    TreeNode val15 = new TreeNode(15);
    TreeNode val7 = new TreeNode(7);

    root.left = val9;
    root.right = val20;
    val20.left = val15;
    val20.right = val7;


    levelOrderBottom(root);
}

public static List<List<Integer>> levelOrderBottom(TreeNode root) {
    
    List<List<Integer>> result = new ArrayList<List<Integer>>();
    // BFS

    if (root == null) {
        return result;
    }
    
    // List<Integer> firstResult = new ArrayList<Integer>();
    // firstResult.add(root.val);
    // result.add(firstResult);

    // System.out.println(firstResult);

    Queue<TreeNode> queue = new LinkedList<TreeNode>();
    Queue<Integer> levelQueue = new LinkedList<Integer>();

    queue.add(root);
    levelQueue.add(0);

    int previousLevel = 0;

    List<Integer> currentLevelResult = new ArrayList<Integer>();


    while (!queue.isEmpty()) {
        TreeNode currentNode = queue.poll();
        Integer currentLevel = levelQueue.poll();

        // System.out.println(currentLevel);

        if (currentLevel != previousLevel) {
            // System.out.println(previousLevel);
            // System.out.println(currentLevel);
            previousLevel = currentLevel;
            // System.out.println(currentLevelResult);
            result.add(currentLevelResult);

            // Strong reference....
            currentLevelResult = new ArrayList<Integer>();
        }

        if(currentNode.left != null) {
            Integer nextLevel = currentLevel+1;
            queue.add(currentNode.left);
            levelQueue.add(nextLevel);
        }

        if(currentNode.right != null) {
            Integer nextLevel = currentLevel+1;
            queue.add(currentNode.right);
            levelQueue.add(nextLevel);
        }

        currentLevelResult.add(currentNode.val);

    }

    result.add(currentLevelResult);





    Collections.reverse(result);

    //System.out.println(result);
    return result;
}
