    public static void main(String[] args) {
	// write your code her

        TreeNode root = new TreeNode(1);
        TreeNode val2 = new TreeNode(2);
        TreeNode val3 = new TreeNode(3);
        TreeNode val5 = new TreeNode(5);
        TreeNode val4 = new TreeNode(4);

        root.left = val2;
        root.right = val3;
        val2.right = val5;
        val3.right = val4;


        rightSideView(root);
    }

    public static List<Integer> rightSideView(TreeNode root) {

        List<Integer> result = new ArrayList<Integer>();

        if(root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        Queue<Integer> levelQueue = new LinkedList<Integer>();

        queue.add(root);
        levelQueue.add(0);

        List<Integer> currentLevelResult = new ArrayList<Integer>();
        Integer previousLevel = 0;

        while(!queue.isEmpty()) {

            TreeNode currentNode = queue.poll();
            Integer currentLevel = levelQueue.poll();


            if (currentLevel != previousLevel) {
                previousLevel = currentLevel;
                result.add(currentLevelResult.get(currentLevelResult.size()-1));
                currentLevelResult = new ArrayList<Integer>();
            }

            if (currentNode.left != null) {
                Integer nextLevel = currentLevel+1;
                queue.add(currentNode.left);
                levelQueue.add(nextLevel);
            }

            if (currentNode.right != null) {
                Integer nextLevel = currentLevel+1;
                queue.add(currentNode.right);
                levelQueue.add(nextLevel);
            }

            currentLevelResult.add(currentNode.val);

        }

        if (currentLevelResult.size()>0) {
            result.add(currentLevelResult.get(currentLevelResult.size()-1));
        }

        System.out.println(result);

        return result;
    }
