/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> List = new ArrayList<>();
        pot(root,List);
        return List;
    }
    
    void pot(TreeNode root, List<Integer> List)
    {
        if(root==null)
        {
            return;
        }
        pot(root.left, List);
        pot(root.right, List);
        List.add(root.val);
    }
}