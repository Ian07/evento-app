import React, { Component } from 'react';
import Dashboard from './components/Dashboard';
import './App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      estaLogueado: localStorage.getItem('token') ? true : false,
      nombreUsuario: '',
      email: '',
      erroresLogin: false,
      erroresSignup: false,
      erroresModificacion: false
    };
  }
  
  //el componente hizo el montaje
  componentDidMount(){
    if(this.state.estaLogueado){
      /* si estamos logueados vamos a traernos a un usuario de
      la base, en este caso, yo tengo a Matias, pero podria ser cualquier cosa */
      fetch('https://8b73abec.ngrok.io/api/v1/usuario_actual/',{
        method: 'GET',
        headers: {
          Authorization: `JWT ${localStorage.getItem('token')}`,
        }
      })
      .then(res => res.json())
      .then(json => {
        this.setState({nombreUsuario: json.username, email: json.email})
      })
    }
  }

  handleLogin = (e, data) => {
    e.preventDefault();
    fetch('https://8b73abec.ngrok.io/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(res => {
        if(res.status === 200){
            res.json().then(json => {
              localStorage.setItem('token', json.access);
              localStorage.setItem('vapid_key', 'BJ2VpiRAu3hAFAD6c9mS83-cSBWdz9tCZqIb5o5SpJRRy3zgpVVLQbjswZv9KU3vYqMEPJfheLETe-c680CXTTQ');
              localStorage.setItem('user_id','1');
              this.setState({
                estaLogueado: true,
                nombreUsuario: json.username,
                email: json.email,
                erroresLogin: false
              });
            });
        } else { //no está autorizado
          this.setState({erroresLogin: "Sus credenciales son incorrectas o el usuario no se encuentra registrado."})
        }
      });
  };

  handleSignup = (e, datos) => {
    e.preventDefault();
    fetch('https://8b73abec.ngrok.io/api/v1/registrar_usuario/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(datos)
    }).then(res => res.json())
      .then(json => {
        if( ! json.error){
          localStorage.setItem('token', json.token.access);
          this.setState({
            estaLogueado: true,
            nombreUsuario: json.username,
            email: json.email,
            erroresSignup: false
          });
        }else{
          this.setState({
            erroresSignup: json.error
          });
        }
      });
  };

  handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('vapid_key');
    localStorage.removeItem('user_id');
    this.setState({ estaLogueado: false, nombreUsuario: '' });
  };

  handleModificarPerfil = (e, datos) => {
    e.preventDefault();
    fetch('https://8b73abec.ngrok.io/api/v1/usuario_actual/',{
      method: 'GET',
      headers: {
        Authorization: `JWT ${localStorage.getItem('token')}`,
      }
    })
      .then(res => res.json())
      .then(json => {
        fetch('https://8b73abec.ngrok.io/api/v1/usuarios/'+ json.persona +'/',{
          method: 'PUT',
          headers: {
            Authorization: `JWT ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(datos)
        }).then(res => res.json())
          .then(json => {
            if (! json.error) {
              localStorage.removeItem('token');
              this.setState({ estaLogueado: false, nombreUsuario: '', email: '' });
            } else {
              this.setState({
                erroresModificacion: json.error
              });
            }
          })
      })
  };

  render(){
    return <Dashboard 
    estaLogueado={this.state.estaLogueado} 
    nombreUsuario={this.state.nombreUsuario}
    emailUsuario={this.state.email}
    handleLogin={this.handleLogin}
    erroresLogin={this.state.erroresLogin}
    handleSignup={this.handleSignup}
    erroresSignup={this.state.erroresSignup}
    handleLogout={this.handleLogout}
    handleModificarPerfil={this.handleModificarPerfil}
    erroresModificacion={this.state.erroresModificacion}
    />
  }
}

export default App;
