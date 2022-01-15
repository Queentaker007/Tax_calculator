# Tax_calculator
- Your Task is to create a class called person, each person has a name and income
- The income should be private
- You should implement the function get_income, so that one can see the persons income
- You should also implement the function taxes that shows how much taxes this personna has to pay
- In this state taxing is progressive ( see example below)to do this you should use the dictonary with given called "tax_brackets" so that you can calculate the tax
- The dictionary tax_brackets = 
                
                {20000: 0.05,
                
                35000: 0.10,
                
                60000: 0.125,
                
                90000: 0.15,
                
                150000: 0.20,
                
                350000: 0.25}
## Example: Person A earns 100000
The first 20000 aren't taxed

Earnings from 20,000 to 35000 are taxed with 5% 15000*.05=750

Earnings from 35,000 to 60,000 are taxed with 10% 25000*.10=2500

Earnings from 60,000 to 90,000 are taxed with 12.5% 30000*.125=3750

The earnings, the remaing 10,000 are taxed with 15% 10000*.15=1500

This personna has to pay 8500$.

