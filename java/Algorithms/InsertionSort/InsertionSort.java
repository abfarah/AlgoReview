/* 
 * By Abdullahi Farah
 * Basic Insertion sort function
 *
 */

import java.util.Arrays;

public class InsertionSort {
	public static int[] iterativeSort(int[] arr){
		for(int j = 0; j < arr.length; j++){
			int temp = arr[j];
			int i = j-1;
			while(i>=0 && arr[i] > temp){
				arr[i+1] = arr[i];
				i = i-1;
			}
			arr[i+1] = temp;
		}
		return arr;
	}

	public static void main(String[] args){
		int[] arr = {5, 2, 4, 6, 1, 3};
		arr = iterativeSort(arr);
		System.out.println(Arrays.toString(arr));
	}
}
