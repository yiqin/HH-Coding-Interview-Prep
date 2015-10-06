    public static void main(String[] args) {
	// write your code here

        TreeLinkNode node1 = new TreeLinkNode(1);
        TreeLinkNode node2 = new TreeLinkNode(2);
        TreeLinkNode node3 = new TreeLinkNode(3);
        TreeLinkNode node4 = new TreeLinkNode(4);
        TreeLinkNode node5 = new TreeLinkNode(5);
        TreeLinkNode node6 = new TreeLinkNode(6);
        TreeLinkNode node7 = new TreeLinkNode(7);

        node1.left = node2;
        node1.right = node3;
        node2.left = node4;
        node2.right = node5;
        node3.left = node6;
        node3.right = node7;

        connect(node1);
    }

    public static void connect(TreeLinkNode root) {

        if (root == null) {
            return;
        }

        // BFS
        Queue<TreeLinkNode> queue = new LinkedList<TreeLinkNode>();
        queue.add(root);

        List<TreeLinkNode> currentArray = new ArrayList<TreeLinkNode>();
        int level = 1;
        int count = 1;

        while(!queue.isEmpty()) {

            TreeLinkNode currentNode = queue.poll();
            currentArray.add(currentNode);
            count--;

            if(count == 0){
                // Build the link.
                for(int i = 0; i<currentArray.size()-1; i++){
                    TreeLinkNode leftNode = currentArray.get(i);
                    TreeLinkNode rightNode = currentArray.get(i+1);
                    leftNode.next = rightNode;

                }
                TreeLinkNode lastNode = currentArray.get(currentArray.size()-1);
                lastNode.next = null;

                // New...
                level = level*2;
                count = level;
                currentArray = new ArrayList<TreeLinkNode>();
            }

            if (currentNode.left != null) {
                queue.add(currentNode.left);
            }

            if (currentNode.right != null) {
                queue.add(currentNode.right);
            }

        }


    }