import React from 'react';
import Grid from '@material-ui/core/Grid';
import Curso from './Curso';

export function CursoGrid(props){
    return(
        <Grid container spacing={3}>
            { props.cursos.map(cursoActual => (
                <Grid item xs={12} sm={6} lg={4} xl={3}>
                <Curso curso={cursoActual} />
                </Grid>
            ))}
        </Grid>
    )
}

export default CursoGrid;