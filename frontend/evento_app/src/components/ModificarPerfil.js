import React, { useState, useEffect } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import PersonIcon from '@material-ui/icons/Person';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import { Paper } from '@material-ui/core';
import { Redirect } from 'react-router-dom';

const useStyles = makeStyles(theme => ({
  '@global': {
    body: {
      backgroundColor: theme.palette.common.white,
    },
  },
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  root: {
    padding: theme.spacing(3, 2),
    backgroundColor: theme.palette.secondary.main
  },
  errorTipo: {
    color: theme.palette.common.white
  }
}));

export default function ModificarPerfil(props) {
  const classes = useStyles();

  const [username, setUsername] = useState(props.nombreUsuario);
  const [email, setEmail] = useState(props.emailUsuario);
  const [password, setPassword] = useState('');

  useEffect(() => {
    setUsername(props.nombreUsuario);
    setEmail(props.emailUsuario);
  }, [props.nombreUsuario, props.emailUsuario])

  if(! props.estaLogueado){
    return <Redirect to="/"/>
  }else{
    return (
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <PersonIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Modificar datos de usuario
          </Typography>
          {props.errores ?
            <Paper className={classes.root}>
              <Typography component="p" className={classes.errorTipo}>
                {props.errores}
              </Typography>
            </Paper>:null
          }
          <form className={classes.form} noValidate onSubmit={e => props.handleModificarPerfil(e, {'username': username, 'email':email, 'password': password})}>
          <TextField
              type="text"
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="email"
              label="Correo Electrónico"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              name="email"
              autoFocus
            />
            <TextField
              type="text"
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="username"
              label="Nombre de Usuario"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              name="username"
              autoFocus
            />
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              name="password"
              label="Contraseña"
              type="password"
              id="password"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Modificar Perfil
            </Button>
          </form>
        </div>
      </Container>
    );
  }
}