package ;
public class Solution {
    public int trap(int[] height) {
        int size = height.length;
        if (size <= 1) {
            return 0;
        }
        int rain_trapped = 0;
        int rain_cumulative = 0;
        int pivot = height[0];

        for (int i = 1; i < (size - 1); i++) {
            if (height[i] >= pivot && height[i] >= height[i + 1]) {
                pivot = height[i];

            }
        }

        return 0;
    }
}