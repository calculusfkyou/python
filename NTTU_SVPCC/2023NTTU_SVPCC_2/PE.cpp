#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        vector<string> words(n);
        vector<string> no_vowel;
        unordered_map<string, int> no_vowel_words;

        for (int i = 0; i < n; i++) {
            cin >> words[i];
            string t = "";
            for (int j = 0; j < words[i].length(); j++) {
                if (words[i][j] != 'A' && words[i][j] != 'E' && words[i][j] != 'I' && words[i][j] != 'O' && words[i][j] != 'U') {
                    t += words[i][j];
                }
            }
            no_vowel.push_back(t);
            no_vowel_words[t] = i;
        }

        string message;
        cin.ignore(); // Ignore the newline character after n input
        getline(cin, message);

        string temp = "";
        for (int i = 0; i < message.length(); i++) {
            temp += message[i];
            if (no_vowel_words.count(temp)) {
                int ind = no_vowel_words[temp];
                if (i != message.length() - 1) {
                    cout << words[ind] << " ";
                } else {
                    cout << words[ind] << endl;
                }
                temp = "";
            }
        }
    }

    return 0;
}
