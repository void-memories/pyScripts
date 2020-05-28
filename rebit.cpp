#include <iostream>
using namespace std;
#define ll long long int
#include <vector> 
#include <map>
#include <string>
#include <stack>

int precedence(char op){ 
    if(op == '+'||op == '-') 
    return 1; 
    if(op == '*'||op == '/') 
    return 2; 
    return 0; 
} 
  
// Function to perform arithmetic operations. 
int applyOp(int a, int b, char op){ 
    switch(op){ 
        case '&': return (a&b); 
        case '|': return (a|b); 
        case '^': return (a^b); 
    } 
} 
  
// Function that returns value of 
// expression after evaluation. 
int evaluate(string tokens){ 
    int i; 
      
    // stack to store integer values. 
    stack <int> values; 
      
    // stack to store operators. 
    stack <char> ops; 
      
    for(i = 0; i < tokens.length(); i++){ 
          
        // Current token is a whitespace, 
        // skip it. 
        if(tokens[i] == ' ') 
            continue; 
          
        // Current token is an opening  
        // brace, push it to 'ops' 
        else if(tokens[i] == '('){ 
            ops.push(tokens[i]); 
        } 
          
        // Current token is a number, push  
        // it to stack for numbers. 
        else if(isdigit(tokens[i])){ 
            int val = 0; 
              
            // There may be more than one 
            // digits in number. 
            while(i < tokens.length() &&  
                        isdigit(tokens[i])) 
            { 
                val = (val*10) + (tokens[i]-'0'); 
                i++; 
            } 
              
            values.push(val); 
        } 
          
        // Closing brace encountered, solve  
        // entire brace. 
        else if(tokens[i] == ')') 
        { 
            while(!ops.empty() && ops.top() != '(') 
            { 
                int val2 = values.top(); 
                values.pop(); 
                  
                int val1 = values.top(); 
                values.pop(); 
                  
                char op = ops.top(); 
                ops.pop(); 
                  
                values.push(applyOp(val1, val2, op)); 
            } 
              
            // pop opening brace. 
            if(!ops.empty()) 
               ops.pop(); 
        } 
          
        // Current token is an operator. 
        else
        { 
            // While top of 'ops' has same or greater  
            // precedence to current token, which 
            // is an operator. Apply operator on top  
            // of 'ops' to top two elements in values stack. 
            while(!ops.empty() && precedence(ops.top()) 
                                >= precedence(tokens[i])){ 
                int val2 = values.top(); 
                values.pop(); 
                  
                int val1 = values.top(); 
                values.pop(); 
                  
                char op = ops.top(); 
                ops.pop(); 
                  
                values.push(applyOp(val1, val2, op)); 
            } 
              
            // Push current token to 'ops'. 
            ops.push(tokens[i]); 
        } 
    } 
      
    // Entire expression has been parsed at this 
    // point, apply remaining ops to remaining 
    // values. 
    while(!ops.empty()){ 
        int val2 = values.top(); 
        values.pop(); 
                  
        int val1 = values.top(); 
        values.pop(); 
                  
        char op = ops.top(); 
        ops.pop(); 
                  
        values.push(applyOp(val1, val2, op)); 
    } 
      
    // Top of 'values' contains result, return it. 
    return values.top(); 
} 

void printTheArray(int arr[], int n) 
{ 
	for (int i = 0; i < n; i++) { 
		cout << arr[i] << " "; 
	} 
	cout << endl; 
} 

void generateAllBinaryStrings(int n, int arr[], int i) 
{ 
	if (i == n) { 
		printTheArray(arr, n); 
		return; 
	} 

	arr[i] = 0; 
	generateAllBinaryStrings(n, arr, i + 1); 

	arr[i] = 1; 
	generateAllBinaryStrings(n, arr, i + 1); 
} 

int main() 
{ 
	ll t,n;
    cin>>t;
    while(t--){
        string s;
        map<string,int> d;
        vector<int> ans;
        ll inc;
        string exp;
        ll arr[100005],brr[100005][100005]={0,0,0,1};
        cin>>s;
        ll unknown=0;

        for(ll i=0;i<s.length();i++)
        {
            if(s[i]=='#')
            unknown++;
        }
        int size = sizeof(brr)/sizeof(*brr);
        for(ll i=0;i<size;i++){
            inc=0;
            exp="";

            for(ll j=0;j<s.length();j++){
                if(s[j]=='#'){
                    exp+=brr[i][inc];
                    inc++;
                }
                else
                exp+=s[j];
            }
            ll temp=evaluate(exp);
            ans.push_back(temp);
            d[to_string(temp)]+=1;

        }

        for(ll i=0;i<ans.size();i++)
        {
            for(ll j=i+1;i<ans.size();j++)
            {
                if (ans[i]==ans[j])
                d[(to_string(ans[i]))]+=1;
            else if (ans[i]==0 and ans[j]==1)
                d["a"]+=1;
            else
                d["A"]+=1;
            }
        }

        for(ll i=ans.size()-1;i>=0;i--)
        {
            for(ll j=ans.size()-2;j>=0;j--)
            {
                if (ans[i]==ans[j])
                d[(to_string(ans[i]))]+=1;
            else if (ans[i]==0 and ans[j]==1)
                d["a"]+=1;
            else
                d["A"]+=1;
            }
        }
        cout<<d["0"]<<d["1"]<<d["a"]<<d["A"]<<" "<<endl;


    }

	return 0; 
} 
