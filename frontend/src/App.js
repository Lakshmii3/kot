// @flow
import React from 'react';
import './App.css';
import 'antd/dist/antd.css'; // or 'antd/dist/antd.less'

import Routers from './containers/Routes'

function App() {
  return (
    <div className="App">
      <Routers />
    </div>
  );
}

export default App;
