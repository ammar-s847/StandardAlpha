import './Stock-Box.css';
import Iframe from 'react-iframe';

function StockBox(props) {
  const chart_Iframe_URL = 'https://ammar-s847.github.io/TradingView-chart-Iframe/stock-chart.html';

  if (props.shares) {
    return (
      <div className="stockbox">
        <h3>{props.symbol}</h3>
        <p>{props.shares} shares</p>
        <Iframe url={`${chart_Iframe_URL}?symbol=${props.symbol}`}
          width="420px"
          height="420px"
          id="myId"
          display="initial"
          position="relative"/>
      </div>
    );
  } else {
    return (
      <div className="stockbox">
        <h3>{props.symbol}</h3>
        <p>no shares in portfolio</p>
        <Iframe url={`${chart_Iframe_URL}?symbol=${props.symbol}`}
          width="420px"
          height="420px"
          id="myId"
          display="initial"
          position="relative"/>
      </div>
    );
  }
}

export default StockBox;