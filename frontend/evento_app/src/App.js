import React, { Component } from 'react';
import Dashboard from './components/Dashboard';
import './App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      estaLogueado: localStorage.getItem('token') ? true : false,
      nombreUsuario: ''
    };
  }
  
  //el componente hizo el montaje
  componentDidMount(){
    if(this.state.estaLogueado){
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
        this.setState({nombreUsuario: json.username})
      })
    }
  }

  handleLogin = (e, data) => {
    e.preventDefault();
    fetch('http://localhost:8000/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.access);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: json.username //falta que el api-token devuelva el nombre de usuario
        });
      });
  };

  handle_signup = (e, data) => {
    e.preventDefault();
    fetch('http://localhost:8000/api/v1/registrar_usuario/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(json => {
        localStorage.setItem('token', json.token.access);
        this.setState({
          logged_in: true,
          displayed_form: '',
          username: json.username
        });
      });
  };

  handle_logout = () => {
    localStorage.removeItem('token');
    this.setState({ logged_in: false, username: '' });
  };

  render(){
    return <Dashboard 
    estaLogueado={this.state.estaLogueado} 
    nombreUsuario={this.state.nombreUsuario}
    handleLogin={this.handleLogin}
    handle_signup={this.handle_signup}
    handle_logout={this.handle_logout}
    />
  }
}

export default App;
