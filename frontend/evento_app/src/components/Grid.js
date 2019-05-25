import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import CursoCard from './CursoCard';
import Grid from '@material-ui/core/Grid';

const styles = theme => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing.unit * 2,
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
});

function CenteredGrid(props) {
  const { classes } = props;

  return (
    <div className={classes.root} style={{padding:24}}>
      <Grid container spacing={24} >
        <Grid item xs={6}>
          <CursoCard nombreCurso="Curso de Linux" descripcion="Super Curso"/>
        </Grid>
        <Grid item xs={6}>
          <CursoCard nombreCurso="Curso de Seguridad" descripcion="Super Curso"/>
        </Grid>
      </Grid>
    </div>
  );
}

CenteredGrid.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(CenteredGrid);