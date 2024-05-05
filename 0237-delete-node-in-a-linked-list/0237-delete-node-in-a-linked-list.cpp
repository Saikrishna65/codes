/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        while (node->next->next)
        {
            // Copy the value of the next node to the current node
            node->val = node->next->val;
            // Move to the next node
            node = node->next;
        }
        // Copy the value of the last node to the current node
        node->val = node->next->val;
        // Remove the last node by setting the next pointer to NULL
        node->next = NULL;
    }
};