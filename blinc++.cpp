
#include <iostream>
#include <cstdlib>

using namespace std;
int main (){
	int flourMin = 300;
	int milkMin = 30;
	int eggMin = 3;
	int eggAm;
	int milkAm;
	int flourAm;
	int n;

	string opCl;

	cout << "Welcome to the BlinMaker. Start the program? Y/N...";
	cin >> opCl;

	if ( opCl == "Y" ){
	
		cout << "\nStarting programm...";
		cout << "\nHow much eggs do you have?...";
		cin >> eggAm;

		cout << "\nHow much milk do you have (ml) ?...";
		cin >> milkAm;

		cout << "\nHow much flour do you have (g) ?...";
		cin >> flourAm;

	if ( eggAm < eggMin ){

		cout << "You don't have enough eggs. You need " << eggMin - eggAm << " more eggs.\n";
 	}
	else if ( flourAm < flourMin ){
		cout << "You don't have enough flour. You need " << flourMin - flourAm << " g of flour more.\n";
 	}
	else if ( milkAm < milkMin ){
		cout "You don't have enough milk. You need " << milkMin - milkAm << " ml milk more.\n";
	}
	
	else {

		cout << "You can make " << n << " amount of pancakes.\n";
	}
}
else {

	cout << "Program closing...\n";
}

system("PAUSE");
return 0;

}

