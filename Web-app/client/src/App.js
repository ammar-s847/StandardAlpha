import './App.css';
import Header from './components/Header.js';
import StockBox from './components/Stock-Box';
import Landing from './components/Landing';

function App() {
  

  const APIData = {
    'userId':'123',
    'username':'Jack',
    'tracking':[
      ['TSLA', 6],
      ['MSFT', 4],
      ['AAPL', 0],
      ['PLTR', 2],
    ]
  };

  return (
    <div className="App">
      <Header />
      <b>Hey {APIData.username}, here's how your portfolio is doing today!</b>



      <h2>Tracked Stocks</h2>
      

      {APIData['tracking'].map((item) => {
        return (<StockBox symbol={item[0]} shares={item[1]}/>)
      })}

      <h2>Pricing Notifiers</h2>

      <h2>Sentimental Analysis</h2>

      <h2>Featured News</h2>
    </div>
  );
}

export default App;