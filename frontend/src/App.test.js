import React from 'react';
import { render, fireEvent, screen, shallow } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  const { getByText } = render(<App />);
  const textElement = getByText(/Select a Sensor/i);
  expect(textElement).toBeInTheDocument();
});


test('renders button', () => {
  const { container, getByText } = render(<App />);
  const button = container.querySelector("button");
  expect(button.innerHTML).toBe("Show Occupance");
});


