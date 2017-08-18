/*Longest increasing subarray*/

#include<iostream>
#include<vector>
#include <utility>
using namespace std;



/* Works in O(n) time complexity*/
pair<int,int> lis(vector<int> &a)
{
	int max = 1;
	int i;
	int length = a.size();
	vector<int> b(a.size());
	b[0] = 1;
	for (i = 1; i < length; ++i)
	{
		if (a[i] > a[i-1])
		{
			b[i] = b[i-1] + 1;
			if (b[i] > max)
			{
				max = i;
			}
		}
		else 
		{
			b[i] = 1;
		}
	}
	return {(max - b[max] + 1), max};
	//cout << "index range: " << ((max+1) - b[max]) <<" " << (max) << endl;
}
 
int main()
{
	pair<int,int> ans;
	vector<int> a = {1,2,3,4,5,6,7,10,9,15,16,17};
	vector<int> b = {13,14,15,1,2,3,4,5,6};
	ans = lis(a);
	cout << "index range: " << ans.first << " "<< ans.second << endl;
	//lis(b);
}
