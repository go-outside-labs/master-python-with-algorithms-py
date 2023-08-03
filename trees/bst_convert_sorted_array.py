#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

# note that there is no unique solution, and different choices
# for the root node would reflect on p is defined


def convert_sorted_array_bst(nums):

      def helper(left, right):
        
            if left > right:
                return None

            p = (left + right) // 2

            root = Node(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)

            return root
        
      return helper(0, len(nums) - 1)
  
