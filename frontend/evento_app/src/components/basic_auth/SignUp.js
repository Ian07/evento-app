import React, { useState } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
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
    marginTop: theme.spacing(3),
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

export default function SignUp(props) {
  const classes = useStyles();

  const [nombre, setNombre] = useState('');
  const [apellido, setApellido] = useState('');
  const [documento, setDocumento] = useState('');
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  if(props.estaLogueado){
    return <Redirect to='/'/>
  }else{
    return (
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Registrarse
          </Typography>
          {props.errores ?
            <Paper className={classes.root}>
              <Typography component="p" className={classes.errorTipo}>
                {props.errores}
              </Typography>
            </Paper>:null
          }
          <form 
            className={classes.form}
            noValidate
            onSubmit={e => props.handleSignup(e, {
              'nombre': nombre,
              'apellido':apellido,
              'documento': documento,
              'email': email,
              'username': username,
              'password': password
            })}
            >
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="nombre"
                  name="nombre"
                  variant="outlined"
                  required
                  fullWidth
                  id="nombre"
                  label="Nombre"
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                  autoFocus
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete="apellido"
                  name="apellido"
                  variant="outlined"
                  required
                  fullWidth
                  id="apellido"
                  label="Apellido"
                  value={apellido}
                  onChange={(e) => setApellido(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  autoComplete="documento"
                  name="documento"
                  variant="outlined"
                  required
                  fullWidth
                  id="documento"
                  label="Documento"
                  type="number"
                  value={documento}
                  onChange={(e) => setDocumento(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  autoComplete="email"
                  name="email"
                  variant="outlined"
                  required
                  fullWidth
                  id="email"
                  label="Correo Electrónico"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  autoComplete="username"
                  name="username"
                  variant="outlined"
                  required
                  fullWidth
                  id="username"
                  label="Nombre de Usuario"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  autoComplete="current-password"
                  name="password"
                  variant="outlined"
                  required
                  fullWidth
                  label="Contraseña"
                  type="password"
                  id="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </Grid>
            </Grid>
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Registrarse
            </Button>
            <Grid container justify="flex-end">
              <Grid item>
                <Link href="#" variant="body2">
                  ¿Ya tenés un cuenta? Inicia Sesión
                </Link>
              </Grid>
            </Grid>
          </form>
        </div>
      </Container>
    );
  }
}