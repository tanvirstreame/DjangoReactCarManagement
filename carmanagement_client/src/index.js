import React from 'react';
import ReactDOM from 'react-dom';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';
import './Styles/index.css';
import CarGetAll from './Components/getAllCar'
import CreateCarForm from './Components/createCarForm';
import GetShowRoomInfo from './Components/getShowRoomInfo';
import GetShowRoom from './Components/getShowRoom';
import Home from './Components/home';
import CreateOwner from './Components/createOwner'
import CreateShowRoomForm from './Components/createShowroom'
import CarAssignShowroom from './Components/carAssignShowroom'
import OwnerAssignShowroom from './Components/ownerAssignShowroom'
import CarInformation from './Components/carInformation'
import Dashboard from './Components/dashboard'
import * as serviceWorker from './serviceWorker';
import 'bootstrap/dist/css/bootstrap.css';
import { Route, BrowserRouter as Router } from 'react-router-dom';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphql/',
});

const routing = (
  <ApolloProvider client={client}>
    <Router>
      <div>
        <Route path="/" component={CreateCarForm} exact/>  
        <Route path="/getallcar" component={CarGetAll} exact/>
        <Route path="/createowner" component={CreateOwner} exact/>
        <Route path="/showroom/" component={GetShowRoom} exact/>
        <Route path="/getshowroominfo/:id" component={GetShowRoomInfo} exact/>
        <Route path="/createshowroomform" component={CreateShowRoomForm} exact/>
        <Route path="/carassignshowroom" component={CarAssignShowroom} exact/>
        <Route path="/ownerassignshowroom" component={OwnerAssignShowroom} exact/>
        <Route path="/getcarinfo/:id" component={CarInformation} exacts/>
      </div>
    </Router>
  </ApolloProvider>
)
ReactDOM.render(routing, window.document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
