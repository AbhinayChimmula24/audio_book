'use client'; // Ensure this is at the top of the file

import * as React from 'react';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import NextLink from 'next/link';
import theme from '@/theme';
 // Adjust the path as necessary

export default function Home() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Box
          sx={{
            my: 4,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <Typography variant="h4" component="h1" sx={{ mb: 2 }}>
            Material UI - Next.js App Router example in TypeScript
          </Typography>
          <Link href="/about" color="secondary" component={NextLink}>
            Go to the about page
          </Link>
        </Box>
      </Container>
    </ThemeProvider>
  );
}
