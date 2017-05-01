/*Design an efficient algorithm for 0 mod n subset problem*/

#include<iostream>
#include<vector>
#include <numeric> 

using namespace std;

vector<int> find_zero_sum_subset(vector<int> &a)
{
	vector<int> prefix_sum(a);
	for (int i = 0; i < a.size(); ++i)
	{
		prefix_sum[i] += i > 0 ? prefix_sum[i-1] : 0;
		prefix_sum[i]	%= a.size();
	}

	vector<int> table(a.size(),-1);
	for (int i = 0; i < a.size(); ++i)
	{
		if (prefix_sum[i] == 0){
			vector<int> ans(i+1);
			iota(ans.begin(), ans.end(), 0);
			return ans;
		}
		else if (table[prefix_sum[i]] != -1)
		{
			vector<int> ans(i-table[prefix_sum[i]]);
			iota(ans.begin(), ans.end(), table[prefix_sum[i]]+1);
			return ans;
		}
		table[prefix_sum[i]] = i;
	}
}


int main()
{
	vector<int> a = {429, 334, 62, 711, 704, 763, 98, 733, 721, 995};
	vector<int> ans = find_zero_sum_subset(a);
	for (auto i = ans.begin(); i != ans.end(); ++i){
    	cout << *i << ' ';
	}
	cout << endl;
}
