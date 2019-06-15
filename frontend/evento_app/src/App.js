import React, { Component } from 'react';
import Dashboard from './components/Dashboard';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      logged_in: localStorage.getItem('token') ? true : false,
      username: ''
    };
  }
  
  //el componente hizo el montaje
  componentDidMount(){
    if(this.state.logged_in){
      /* si estamos logueados vamos a traernos a un usuario de
      la base, en este caso, yo tengo a Matias, pero podria ser cualquier cosa */
      fetch('http://localhost:8000/api/v1/usuario_actual/',{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        this.setState({username: json.username})
      })
    }
  }

  render(){
    return <Dashboard></Dashboard>
  }
}

export default App;
